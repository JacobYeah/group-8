
from math import sqrt
import abc
from builtins import isinstance
import pickle
import numpy as np
import tool

##correlation coefficient
class DataType:
    Like_dislike = 1       # Like, purchase
    Product_rate = 2    # Adding comment

##if one user 
def jaccard(User1, User2):
        # Jaccard similarity is applicable to both list type and dictionary type.
        Intersection = sum([1 for obj in User1 if obj in User2])
        Union = len(User1) + len(User2) - Intersection
        if Union == 0:
            return -1
        return Intersection / Union

def cosine_intersection(User1, User2):
    # if type(dataA) is list and type(dataB) is list:
    if len(User1) != len(User2):
        print("Error: the length of two input lists are not same.")
        return -1
    interSet = [i for i in range(len(User1)) if User1[i] * User2[i] != 0]
    if len(interSet) == 0:
        return 0
    Sum = sum([User1[i] * User2[i] for i in range(interSet)])
    normA = sqrt(sum([User1[i] ** 2 for i in range(interSet)]))
    normB = sqrt(sum([User2[i] ** 2 for i in range(interSet)]))
    denominator = normA * normB
    if denominator == 0:
        return 0
    return Sum / denominator

class Spend_behavior_Prediction(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, dataType = DataType.Like_dislike):
        self.dataType = dataType
        self.prefs = {}
        self.itemList = None

    def loadModel(self, Path):
        print("Loading the model..............")
        try:
            file = open(Path, "rb")
            model = pickle.load(file)
            file.close()
            print("Finish!")
            return model
        except:
            print("Load failed!")
            return None

    def loadData(self, data):
        if isinstance(data, dict):
            self.prefs = data
        elif isinstance(data, str):
            # self.prefs = tool.loadData(data)
            pass
        self.itemList = {}
        for user in self.prefs:
            for item in self.prefs[user]:
                self.itemList[item] = None
    
    def getNearestNeighbors(self, target_user, measure, number_of_neighbours = None):
        similarities = [(measure(self.prefs[target_user], self.prefs[other_user]), other_user) for other_user in self.prefs if target_user != other_user]
        ## sort the similarity between other users
        similarities.sort(reverse = True)
        if number_of_neighbours != None:
            similarities = similarities[0:number_of_neighbours]
        return similarities
    
    def buildModel(self, measure, nNeighbors = None, Path = None):
        # Model contains top-K similar users for each user and their similarities.
        # Model format: {user: [(similarity, neighbor), ...], ...}
        model = self.loadModel(Path)
        if model != None:
            return model
        
        print("Now running the model.........")
        model = {}
        for user in self.prefs:
            model[user] = self.getNearestNeighbors(user, measure, nNeighbors)
        # if pathDump != None:
        #     self.dumpModel(model, pathDump)
        print("\tComplete!")
        return model

    def get_predict_rate(self, user, product, nearestNeighbors):
        # nearestNeighbors = self.getNearestNeighbors(user, jaccard)
        if self.dataType == DataType.Like_dislike:
            if product in self.prefs[user]:
                return 1.0
            similarities = [similarity for neighbor, similarity in nearestNeighbors.items() if product in self.prefs[neighbor]]
            if len(similarities) == 0:
                return 0.0
            return np.mean(similarities)
        
        elif self.dataType == DataType.Product_rate:
            if product in self.prefs[user]:
                return self.prefs[user][product]
            mean_rate = np.mean([score for score in self.prefs[user].values()])
            weightedSum = 0
            normalizingFactor = 0
            for neighbor, similarity in nearestNeighbors.items():
                if product not in self.prefs[neighbor]:
                    continue
                meanRatingOfNeighbor = np.mean([r for r in self.prefs[neighbor].values()])
                weightedSum += similarity * (self.prefs[neighbor][product] - meanRatingOfNeighbor)
                normalizingFactor += np.abs(similarity)
            if normalizingFactor == 0:
                return 0
            return mean_rate + (weightedSum / normalizingFactor)

    def Recommendation(self, user, measure = jaccard, nNeighbors = 50, model = None, topN = None):
        if model != None:
            '''
            If a user-user similarity model is given,
            other parameters such as similarity measure and the number of nearest neighbors are ignored.
            It is because that the similarity measure and # of neighbors are determined during the model building.
            '''
            candidateItems = {}         # List of candidate items to be recommended
            nearestNeighbors = {}       # List of nearest neighbors
            for similarity, neighbor in model[user]:
                if similarity <= 0:
                    break
                nearestNeighbors[neighbor] = similarity
                for product in self.prefs[neighbor]:
                    candidateItems[product] = None
            predictedScores = [(self.get_predict_rate(user, product, nearestNeighbors), product)
                               for product in candidateItems if product not in self.prefs[user]]
        else:
            '''
            If a model is not given, the recommendation task follows the original CF method.
            After finding K-nearest neighbors who have rating history on the item,
            the recommendation is made by using their similarities.
            '''
            predictedScores = []        # predictedScores = [(predicted_score, item), ...]
            similarities = self.getNearestNeighbors(user, measure)   # similarities = [(similarity, neighbor), ...]
            for product in self.itemList:
                if product in self.prefs[user]:
                    continue
                productRaters = {}         # Nearest neighbors who rated on the item
                for similarity, neighbor in similarities:
                    if similarity <= 0 or len(productRaters) == nNeighbors:
                        break
                    if product in self.prefs[neighbor]:
                        productRaters[neighbor] = similarity
                predictedScores.append((self.get_predict_rate(user, product, productRaters), product))
        
        predictedScores.sort(reverse = True)
        recommendation = [product for similarity, product in predictedScores]
        if topN != None:
            recommendation = recommendation[0:topN]
        return recommendation
