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
              <td>Day:</td>
              <td>{{ county.day }}</td>
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

    <div>
      <ul>
        <li><button><a href="http://localhost:5000/debug/advance_day">Advance Day</a></button></li>
        <li><button><a href="http://localhost:5000/debug/buy_footman">Buy Footman</a></button></li>
        <li><button><a href="http://localhost:5000/debug/buy_archer">Buy Archer</a></button></li>
      </ul>
    </div>
  </div>
</template>

<script>
import countiesApi from '@/api/counties-api';
import systemApi from '@/api/system-api';

export default {
  name: 'CountyHome',
  components: {},
  props: {},
  data() {
    return {
      user: {},
      county: {},
      loading: false,
    };
  },
  computed: {},
  mounted() {
    this.loading = true;
    this.loadCurrentUser()
    .finally(() => {
      this.loading = false;
    });
  },
  methods: {
    loadCurrentUser () {
      return systemApi.currentUser().then(({ user }) => {
        if (!user.id) {
          this.$router.push('/session/login')
          return
        }

        this.user = user
        return countiesApi.fetch(user.countyId).then(({ county }) => {
          this.county = county
        })
        .catch((response) => console.log('response', response))

      })
      .catch((response) => console.log('response', response))
    },
  },
};
</script>

<style scoped></style>
