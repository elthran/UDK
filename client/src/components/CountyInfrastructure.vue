<template>
  <div v-if="!loading">
    <div class="content flex-container">
      <div
        style="margin: 5px; min-width: 600; order: 1; padding: 5px 5px 5px 5px;
        border: 3px solid rgba(139, 18, 59, 1);">
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
</style>
