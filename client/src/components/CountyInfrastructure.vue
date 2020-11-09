<template>
  <div v-if="!loading">
    <ul>
      <li
        v-for="building in infrastructure.buildings"
        :key="building.id"
        style="font-size:20px"
      >{{ building.className }}. Costs: {{ building.goldCost }} gold,
        {{ building.woodCost }}
        wood, and {{ building.stoneCost }} stone. {{ building.description }}
      </li>
    </ul>

    <br>Total employed workers: {{ infrastructure.employedWorkers }} people / {{
      county.population
    }}
  </div>
</template>

<script>
import countyApi from '@/api/counties-api';
import infrastructureApi from '@/api/infrastructure-api';

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
  computed: {
    infrastructure() {
      return this.county.infrastructure;
    },
  },
  mounted() {
    this.loading = true;
    Promise.all([countyApi.fetch(1), infrastructureApi.fetch(1)])
      .then(([{ county }, { infrastructure }]) => {
        Object.assign(this.county, county);
        Object.assign(this.county.infrastructure, infrastructure);
      })
      .finally(() => {
        this.loading = false;
      });
  },
};
</script>

<style scoped>
</style>
