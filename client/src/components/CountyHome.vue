<template>
  <div v-if="!loading">
    <div class="content flex-container">
      <div
        style="margin: 5px; min-width: 600; order: 2;
          padding: 5px 5px 5px 5px; border: 3px solid rgba(139, 18, 59, 1);"
      >
        <table>
          <tr>
            <td><img src="@/assets/images/example_image.jpeg"/></td>
            <td>
              <table>
                <tr>
                  <td>Leader:</td>
                  <td>{{ county.title }} {{ county.leader }}</td>
                </tr>
                <tr>
                  <td>Race:</td>
                  <td>{{ county.race }}</td>
                </tr>
                <tr>
                  <td>Background:</td>
                  <td>{{ county.background }}</td>
                </tr>
                <tr>
                  <td>Population:</td>
                  <td>{{ county.economy._population }} people</td>
                </tr>
                <tr>
                  <td>Land:</td>
                  <td>{{ county.economy._land }} acres</td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
        <!--
        <ul>
          <li>Leader: {{ county.title }} {{ county.leader }}</li>
          <li>Race: {{ county.race }}</li>
          <li>Background: {{ county.background }}</li>
          <li>Population: {{ county.population }}</li>
          <li>Land: {{ county.land }} acres</li>
        </ul>
        !-->
      </div>
      <div
        style="
            margin: 5px; min-width: 600; order: 3;
            padding: 5px 5px 5px 5px; border: 3px solid rgba(139, 18, 59, 1);"
      >
        <p>
          Your subjects are
          {{ county.economy.happiness >= 100 ? "Very Happy!" : "Happy" }}
        </p>
        <br/>
        <p>
          You currently have the following resources:<br/>{{
            county.economy._wood
          }}
          Wood, {{ county.economy._stone }} Stone,
          {{ county.economy._iron }} Iron, and
          {{ county.economy._gold }} Gold.
        </p>
      </div>
      <div
        style="margin: 5px; min-width: 600; order: 4;
          padding: 5px 5px 5px 5px; border: 3px solid rgba(139, 18, 59, 1);"
      >
        <p>
          {{ county.title }} {{ county.leader }} rules this land wisely,
          perhaps because his {{ county.background }}ly education. Within his
          {{ county.land }} acres he has {{ county.population }} loyal
          subjects.
        </p>
      </div>
      <div class="flex-container-2" style="order: 5">
        <div class="data-block" style="order: 0;">
          <p>DATA 1</p>
          <br/>
          <h1>Looking at all possible preferences</h1>

          <pre>
              {{ JSON.stringify(county.preference, null, 2) }}
            </pre>
        </div>
        <div class="data-block" style="order: 1;">
          <p>DATA 2</p>
          <br/>
          <h1>Looking at all possible economy properties:</h1>

          <pre>
              {{ JSON.stringify(county.economy, null, 2) }}
            </pre>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/api/counties-api';

export default {
  name: 'CountyHome',
  components: {},
  props: {},
  data() {
    return {
      user: {},
      county: {
        economy: {},
      },
      loading: false,
    };
  },
  computed: {},
  mounted() {
    this.loading = true;
    api
      .fetch(1)
      .then(({ county }) => {
        Object.assign(this.county, county);
      })
      .finally(() => {
        this.loading = false;
      });
  },
  methods: {
    urlFor(name) {
      return `/${name}`;
    },
  },
};
</script>

<style scoped>
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
