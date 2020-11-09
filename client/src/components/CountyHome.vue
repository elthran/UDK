<template>
  <div v-if="!loading">
    <div class="content flex-container">
      <div class="flex-container-2" style="margin: 5px; min-width: 600; order: 0;
       padding: 5px 5px 5px 5px; border: 3px solid rgba(139, 18, 59, 1);">
        <div style="flex-basis: 200; order: 0;">
          <img src="@/assets/images/example_image.jpeg"/>
        </div>

        <div style="flex-basis: 400; order: 1;">
          <table>
            <tr>
              <p style="font-size:100px">{{ county.name }}</p>
            </tr>
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
              <td>{{ county.population }} people</td>
            </tr>
            <tr>
              <td>Land:</td>
              <td>{{ county.land }} acres</td>
            </tr>
          </table>
        </div>
      </div>
      <div style="margin: 5px; min-width: 600; order: 1; padding: 5px 5px 5px 5px;
      border: 3px solid rgba(139, 18, 59, 1);">
        <p>Your subjects are Very Happy!</p>
        <br/>
        <p> You currently have the following resources:<br/>{{ county.wood }} Wood,
          {{ county.stone }} Stone, {{ county.iron }} Iron, and {{ county.gold }} Gold.</p>
      </div>
      <div
        style="margin: 5px; min-width: 600; order: 2; padding: 5px 5px 5px 5px;
        border: 3px solid rgba(139, 18, 59, 1);">
        <p>{{ county.title }} {{ county.leader }} rules this land wisely,
          perhaps because his {{ county.background }}ly education.
          Within his {{ county.land }} acres he has {{ county.population }} loyal subjects.</p>
      </div>
      <div class="flex-container-2" style="order: 3">
        <div class="data-block" style="order: 0;">
          <h1>All County Data</h1>
          <p>{{ county }}</p>
          <br/>
        </div>
        <div class="flex-container-2" style="order: 3">
          <div class="data-block" style="order: 0;">
            <h1>All User Data</h1>
            <p>{{ user }}</p>
            <br/>
          </div>
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
  background-color: rgba(220, 186, 96, 1.0);
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

a:link, visited, hover, active {
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

div.nav-bar table tr td {
  padding-top: 3px;
  padding-bottom: 3px;
}

.flex-container {
  display: flex;
  flex-direction: column
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

table.infrastructure tr td, th {
  border: 1px solid black;
  padding: 5px 5px 5px 5px;
}

table.odd {
}

table.odd tr td, th {
  border: 1px solid #ccc;
  padding: 5px;
}

table.odd tr:nth-child(2n+1) {
  background: #f1f1f1;
}

table.people tr td, th {
  border: 1px solid #000000;
  padding: 5px 5px 5px 5px;
}

.value-cell {
  text-align: center;
}

</style>
