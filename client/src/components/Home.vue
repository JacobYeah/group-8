<template>
    <div>
    <b-jumbotron header="Recommend for you">
      <b-button variant="primary" @click="get_recommend()">refresh</b-button>
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
          <img v-if="product==='p1'" :src="images[0]" :key="image">
          <img v-if="product==='p2'" :src="images[1]" :key="image">
          <img v-if="product==='p3'" :src="images[2]" :key="image">
          <img v-if="product==='product1'" :src="images[3]" :key="image">
          <img v-if="product==='product2'" :src="images[4]" :key="image">
          <img v-if="product==='product3'" :src="images[5]" :key="image">
        </template>
        <b-carousel-slide-caption>
          <h2>{{product}}</h2>
        </b-carousel-slide-caption>
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

            <b-button href="#" variant="primary">buy</b-button>
          </b-card>
        </li>
      </ul>
    </b-container>
    </div>
</template>

<script>
import axios from 'axios';
import BScroll from "better-scroll";

export default {
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      images: [
        "https://picsum.photos/1024/480/?image=52",
        "https://picsum.photos/1024/480/?image=58",
        "https://picsum.photos/1024/480/?image=55",
        "https://picsum.photos/1024/480/?image=10",
        "https://picsum.photos/1024/480/?image=12",
        "https://picsum.photos/1024/480/?image=22",
      ],
      // images: [
      //     { url: 'https://picsum.photos/1024/480/?image=52', alt: 'I love you nature' },
      //     { url: 'https://picsum.photos/1024/480/?image=58', alt: 'Now with dog - Rosé' },
      //     { url: 'https://picsum.photos/1024/480/?image=55', alt: 'Jeg er i Danmark' },
      // ],
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
    },
     personScroll() {
      let width = 6 * 120;
      this.$refs.personTab.style.width = width + "px";
      this.$nextTick(() => {
        if (!this.scroll) {
          this.scroll = new BScroll(this.$refs.personWrap, {
            startX: 0,
            click: true,
            scrollX: true,
            scrollY: false,
            eventPassthrough: "vertical"
          });
        } else {
          this.scroll.refresh();
        }
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
