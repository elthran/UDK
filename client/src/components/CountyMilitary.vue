<template>
  <div v-if="!loading">
    <div class="content flex-container">
      <div
        style="margin: 5px; min-width: 600; order: 1; padding: 5px 5px 5px 5px;
        border: 3px solid rgba(139, 18, 59, 1);">
        <p style="font-size: 48px;">{{ county.race }}</p>
        
        <table class="military">
          <tr>
            <th>Unit</th>
            <th>Costs</th>
            <th>Attack</th>
            <th>Defence</th>
            <th>Health</th>
            <th>Description</th>
          </tr>
          <tr
            v-for="unit in county.units"
            :key="unit.id"
            style="font-size:20px"
          >
            <td>{{ unit.className }}</td>
            <td>{{ unit.goldCost }} Go; {{ unit.ironCost }} Ir, {{ unit.woodCost }} Wo</td>
            <td>{{ unit.attack }}</td>
            <td>{{ unit.defence }}</td>
            <td>{{ unit.health }}</td>
            <td>{{ unit.description }}</td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>

import countyApi from '@/api/counties-api';

export default {
  name: 'CountyMilitary',
  components: {},
  props: {},
  data() {
    return {
      user: {},
      county: {
        economy: {},
        preference: {},
        infrastructure: {},
        units: {},
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

<style scoped></style>
