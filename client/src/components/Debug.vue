<template>
  <div v-if="!loading">
    <button><a href="/temp/admin/advance_day">Advance Day</a></button>
    <button><a href="/temp/admin/buy_footman">Buy 1 footman</a></button>
    <button><a href="/temp/admin/buy_archer">Buy 1 archer</a></button>
    <div class="content flex-container">
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
    <div class="flex-container-2" style="order: 3">
      <div class="data-block" style="order: 0;">
        <h1>All Building Data</h1>
        <p>{{ county.buildings }}</p>
        <br/>
      </div>
      <div class="data-block" style="order: 0;">
        <h1>All Army Data</h1>
        <p>{{ county.units }}</p>
        <br/>
      </div>
    </div>
  </div>
</template>

<script>
import countyApi from '@/api/counties-api';
import userApi from '@/api/users-api';

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
    Promise.all([countyApi.fetch(1), userApi.fetch(1)])
      .then(([{ county }, { user }]) => {
        Object.assign(this.county, county);
        Object.assign(this.user, user);
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

<style scoped></style>
