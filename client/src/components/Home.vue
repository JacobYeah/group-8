<template>
    <div>
    <b-jumbotron header="Recommend for you">
      <b-button variant="outline-dark" @click="get_recommend()">refresh</b-button>
    </b-jumbotron>

    <b-container fluid="sm">
      <b-carousel id="carousel1"
                  style="text-shadow: 1px 1px 2px #333;"
                  controls
                  indicators
                  background="#ffffff"
                  :interval="4000"
                  img-width="1024"
                  img-height="480"
                  v-model="slide"
                  @sliding-start="onSlideStart"
                  @sliding-end="onSlideEnd"
      >

      <b-carousel-slide v-for="product in recomms" :key="product.id">
        <template v-slot:img>
          <!-- <img v-for="image in images" :key="image.url" v-bind:src="image.url" v-bind:alt="image.alt" /> -->
          <b-img v-if="product==='p1'" :src="images[0].src" :key="image" rounded></b-img>
          <b-img v-if="product==='p2'" :src="images[1].src" :key="image" rounded></b-img>
          <b-img v-if="product==='p3'" :src="images[2].src" :key="image" rounded></b-img>
          <b-img v-if="product==='product1'" :src="images[3].src" :key="image" rounded></b-img>
          <b-img v-if="product==='product2'" :src="images[4].src" :key="image" rounded></b-img>
          <b-img v-if="product==='product3'" :src="images[5].src" :key="image" rounded></b-img>
        </template>
        <b-carousel-slide-caption>
          <h2>{{product}}</h2>
        </b-carousel-slide-caption>
        <b-carousel-slide-text>
          <p>{{product==='p1' ? images[0].caption: product==='p2' ? images[1].caption: product==='p3' ? images[2].caption: 'null'}}</p>
        </b-carousel-slide-text>
        <b-button href="#" variant="outline-light">buy</b-button>
      </b-carousel-slide>

      </b-carousel>
    </b-container>

    <b-jumbotron header="All Products"></b-jumbotron>

    <b-container fluid="lg">
      <ul>
        <li v-for="item in items" :key="item.title">
          <b-card img-src="https://placekitten.com/g/300/450" img-alt="Card image" img-left class="mb-3">
            <b-card-text>
              <h2>{{item.title}}</h2>
            </b-card-text>

            <b-button href="#" variant="light">buy</b-button>
          </b-card>
        </li>
      </ul>
    </b-container>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      images: [
        {src: "https://picsum.photos/1024/480/?image=52", caption: "hello1"},
        {src: "https://picsum.photos/1024/480/?image=58", caption: "hello2"},
        {src: "https://picsum.photos/1024/480/?image=55", caption: "hello3"},
        {src: "https://picsum.photos/1024/480/?image=10", caption: "hello4"},
        {src: "https://picsum.photos/1024/480/?image=12", caption: "hello5"},
        {src: "https://picsum.photos/1024/480/?image=22", caption: "hello6"},
      ],
      recomms: ['p1','p2','p3'],
      items: [
        {title: 'item1', description: 'item1-description'},
        {title: 'item2', description: 'item2-description'},
        {title: 'item3', description: 'item3-description'},
        {title: 'item4', description: 'item4-description'}
      ],
      slide: 0,
      sliding: null,
    }
  },
  created() {
    this.$nextTick(() => {
      this.personScroll();
    });
  },
  methods: {
    onSlideStart (slide) {
      this.sliding = true
    },
    onSlideEnd (slide) {
      this.sliding = false
    },
    get_recommend() {
      const getRecommend_url = 'http://localhost:5000/'
      axios.get(getRecommend_url, {
                    params: {
                        customer_id: '1'
                    }
                })
                .then((response) => {
                                    console.log(this.recomms);
                  this.recomms = response.data;
                  console.log(this.recomms);
                })
                .catch(function (error) {
                  console.log(error);
                });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
