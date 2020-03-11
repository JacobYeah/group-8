<template>
    <div>
    <b-jumbotron header="Recommend for you"></b-jumbotron>

    <b-container fluid="sm">
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
        <li v-for="item in items" :key="item.title">
          <b-carousel-slide
            img-src="https://picsum.photos/1024/480/?image=58"
          >
            <b-carousel-slide-caption>
              <h2>{{item.title}}</h2>
            </b-carousel-slide-caption>
            <b-carousel-slide-text>
              {{item.description}}
            </b-carousel-slide-text>
          </b-carousel-slide>
        </li>
      </ul>
      </b-carousel>
    </b-container>

    <b-jumbotron header="All Products"></b-jumbotron>

    <b-container fluid="lg">
      <ul>
        <li v-for="item in items" :key="item.title">
          <b-card img-src="https://placekitten.com/g/300/450" img-alt="Card image" img-left class="mb-3">
            <b-card-text>
              <h2>{{item.title}}</h2>
              <p>{{item.description}}</p>
            </b-card-text>

            <b-button href="#" variant="primary">buy</b-button>
          </b-card>
        </li>
      </ul>
    </b-container>
    </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      items: [
        {title: 'item1', description: 'item1-description'},
        {title: 'item2', description: 'item2-description'},
        {title: 'item3', description: 'item3-description'},
        {title: 'item4', description: 'item4-description'}
      ],
      slide: 0,
      sliding: null
    }
  },
  methods: {
    onSlideStart (slide) {
      this.sliding = true
    },
    onSlideEnd (slide) {
      this.sliding = false
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
