<template>
  <div v-if="!loading">
    <div class="content flex-container">
      <div
        style="margin: 5px; min-width: 600; order: 1; padding: 5px 5px 5px 5px;
        border: 3px solid rgba(139, 18, 59, 1);">
        <p style="font-size: 48px;">{{ county.race }}</p>
        <table class="infrastructure">
          <tr>
            <th>Name</th>
            <th>Costs</th>
            <th>Description</th>
          </tr>
          <tr
            v-for="building in county.buildings"
            :key="building.id"
            style="font-size:20px"
          >
            <td>{{ building.className }}</td>
            <td>{{ building.goldCost }} gold, {{ building.woodCost }} wood,
              and {{ building.stoneCost }} stone
            </td>
            <td>{{ building.description }}</td>
          </tr>
        </table>
        <br>Total employed workers: {{ county.employedWorkers }} people / {{ county.population }}
      </div>
    </div>
  </div>
</template>

<script>

import countyApi from '@/api/counties-api';

export default {
  name: 'CountyEconomy',
  components: {},
  props: {},
  data() {
    return {
      user: {},
      county: {
        economy: {},
        preference: {},
        infrastructure: {},
      },
      loading: false,
    };
  },
  mounted() {
    this.loading = true;
    Promise.all([countyApi.fetch(1)])
      .then(([{ county }]) => {
        Object.assign(this.county, county);
      })
      .finally(() => {
        this.loading = false;
      });
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
