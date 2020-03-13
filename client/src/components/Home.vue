<template>
    <div>
    <b-jumbotron header="Recommend for you">
      <b-button variant="primary" @click="get_recommend()">refresh</b-button>
    </b-jumbotron>

    <b-container fluid="sm">
      <div class="person-wrap" ref="personWrap">
          <ul>
            <li v-for="product in recomms" :key="product">
              <p>{{product}}</p>

            </li>
          </ul>
      </div>
    </b-container>

    <!-- <b-container fluid="sm">
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        controls
        indicators
        background="#ffffff"
        img-width="1024"
        img-height="480"
        style="text-shadow: 1px 1px 2px #333;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >

      <ul>
        <li v-for="product in recomms" :key="product">
          <b-carousel-slide
            img-src="https://picsum.photos/1024/480/?image=58"
          >
            <b-carousel-slide-caption>
              <h2>{{product}}</h2>
            </b-carousel-slide-caption>
          </b-carousel-slide>
        </li>
      </ul>
      </b-carousel>
    </b-container> -->

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
      items: [
        {title: 'item1', description: 'item1-description'},
        {title: 'item2', description: 'item2-description'},
        {title: 'item3', description: 'item3-description'},
        {title: 'item4', description: 'item4-description'}
      ],
      recomms: ['p1','p2','p3'],
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
