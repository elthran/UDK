<template>
  <div v-if="!loading">
    <div class="content flex-container">
      <div class="" style="margin: 15px auto; order: 1;">
        <button @click="kingdomWest" :disabled="disableWest">West</button>
        <span style="margin: 0px 30px 0px 30px;">{{ selectedKingdom.name }}</span>
        <button @click="kingdomEast" :disabled="disableEast">East</button>
      </div>
      <div class="" style="margin: auto; order: 2;">
        <br>
        <ul>
              <li
                v-for="county in selectedKingdom.counties"
                :key="county.id"
              >
                {{ county.name }} led by <strong>{{ county.title }} {{ county.leader }}</strong>
                with {{ county.land }} acres
              </li>
        </ul>
      </div>
      <div class="" style="margin: auto; order: 3;">
        <table>
          <tr>
            <th style="border: none;">Heraldry</th>
            <th style="border: none;">County</th>
            <th style="border: none;">Led by</th>
            <th style="border: none;">Acreage</th>
            <th style="border: none;">People</th>
          </tr>
          <tr
            v-for="county in selectedKingdom.counties"
            :key="county.id"
          >
            <td><img src="" alt="heraldry?" width="100" height="100" /></td>
            <td>{{ county.name }}</td>
            <td>{{ county.title }} {{ county.leader }}</td>
            <td>{{ county.land }} acres</td>
            <td>{{ county.population }}</td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import kingdomsApi from '@/api/kingdoms-api';
import systemApi from "@/api/system-api";

export default {
  name: 'Kingdom',
  components: {},
  props: {},
  data() {
    return {
      kingdoms: [],
      kingdomIndex: null,
      loading: false,
    };
  },
  computed: {
    disableWest() {
      return this.kingdomIndex === 0
    },
    disableEast() {
      return this.kingdomIndex === this.kingdoms.length - 1
    },
    selectedKingdom() {
      return this.kingdoms[this.kingdomIndex]
    }
  },
  mounted() {
    this.loading = true

    kingdomsApi.fetchAll()
      .then(({ kingdoms }) => {

        this.kingdoms = kingdoms

        systemApi.currentKingdom()
        .then(({ kingdom }) => {
          this.kingdomIndex = this.kingdoms.findIndex((k) => k.id === kingdom.id)
        })
        .finally(() => {
          this.loading = false
        });
      })

  },
  methods: {
    kingdomWest() {
      this.kingdomIndex = this.kingdomIndex - 1
    },
    kingdomEast() {
      this.kingdomIndex = this.kingdomIndex + 1
    }
  }
};
</script>

<style scoped></style>
