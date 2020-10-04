<template lang="pug">
  #county-interface(v-if="!loading")
    div(style="margin: 5px; min-width: 600; order: 1; padding: 5px 5px 5px 5px; border: 3px solid rgba(139, 18, 59, 1);")
      h1 The County object is {{ county }}
      h1 The User object is {{ user }}
      br
    div(style="margin: 5px; min-width: 600; order: 2; padding: 5px 5px 5px 5px; border: 3px solid rgba(139, 18, 59, 1);")
      table
        tr
          td #[img(src="/static/images/example_image.jpeg")]
          td
            table
              tr
                td Leader:
                td {{ county.title }} {{ county.leader }}
              tr
                td Race:
                td {{ county.race }}
              tr
                td Background:
                td {{ county.background }}
              //- tr
              //-   td Population:
              //-   td {{ county.economy._population }} people
              //- tr
              //-   td Land:
              //-   td {{ county.economy._land }} acres
      <ul>
          <li>Leader: {{ county.title }} {{ county.leader }}</li>
          <li>Race: {{ county.race }}</li>
          <li>Background: {{ county.background }}</li>
          <li>Population: {{ county.population }}</li>
          <li>Land: {{ county.land }} acres</li>
      </ul>
    //- div(style="margin: 5px; min-width: 600; order: 3; padding: 5px 5px 5px 5px; border: 3px solid rgba(139, 18, 59, 1);")
    //-   p Your subjects are {{ county.economy._happiness >= 100 ? 'Very Happy!': 'Happy' }}
    //-   br
    //-   p You currently have the following resources:
    //-   p {{ county.economy._wood }} Wood, {{ county.economy._stone }} Stone, {{ county.economy._iron }} Iron, and {{ county.economy._gold }} Gold.
    div(style="margin: 5px; min-width: 600; order: 4; padding: 5px 5px 5px 5px; border: 3px solid rgba(139, 18, 59, 1);")
      p {{ county.title }} {{ county.leader }} rules this land wisely, perhaps because his {{ county.background }}ly education. Within his {{ county.land }} acres he has {{ county.population }} loyal subjects.
    div(class="flex-container-2" style="order: 5")
      div(class="data-block" style="order: 0;")
        p DATA 1
        br
        h1 Looking at all possible generic county properties:

        ul(v-for="attribute in county.__dict__")
          li {{ attribute }}
      //- div(class="data-block" style="order: 1;")
      //-   p DATA 2
      //-   br
      //-   h1 Looking at all possible economy properties:

      //-   ul(v-for="attribute in county.economy.__dict__")
      //-     li {{ attribute }}

</template>

<script>
import api from '@/api/county-api'

export default {
  name: 'CountyInterface',
  components: {},
  props: {},
  data () {
    return {
      county: {},
      user: {
        id: 77,
        fullName: 'Marlen',
      },
      loading: false,
    }
  },
  computed: {},
  mounted () {
    this.loading = true
    api
      .fetch(1)
      .then(county => {
        this.county = count
      })
      .finally(() => {
        this.loading = false
      })
  },
  methods: {},
}
</script>

<style lang="scss" scoped>
body {
  background-color: rgba(220, 186, 96, 1);
}

div.nav-bar {
  flex-basis: 400;
  flex-shrink: 0;

  margin: 20px;
  padding: 10px 10px 10px 10px;
  border: 3px solid rgba(139, 18, 59, 1);
  border-radius: 5px;

  background-color: rgba(251, 246, 224, 1);
}

a {
  font-size: large;
}

div.content {
  max-width: 800;
  margin: 20px;
  border-style: solid;
  border-width: 3px;
  border-radius: 5px;
  border-color: rgba(139, 18, 59, 1);
  background-color: rgba(251, 246, 224, 1);
}

div.data-block {
  flex-basis: 600px;
  flex-grow: 1;
  flex-shrink: 1;
  margin: 5px;
  padding: 10px;
  border: 3px solid rgba(139, 18, 59, 1);
}

a:link,
visited,
hover,
active {
  text-decoration: none;
  color: rgba(4, 56, 93, 1);
}

a:visited {
  text-decoration: none;
  color: rgba(4, 56, 93, 1);
}

a:hover {
  text-decoration: none;
  color: rgba(4, 56, 93, 1);
}

a:active {
  text-decoration: none;
  color: rgba(4, 56, 93, 1);
}

.page {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
}

.page table {
  margin: 5px;
}

.flex-container {
  display: flex;
  flex-direction: column;
}

.flex-container-2 {
  display: flex;
  flex-direction: row;
}

h3 {
  font-size: medium;
  font-weight: bold;
  text-align: left;
}
</style>
