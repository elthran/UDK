<template>
  <div v-if="!loading">
    <button @click="kingdomWest" :disabled="disableWest">West</button>
    {{ selectedKingdom.name }}
    <button @click="kingdomEast" :disabled="disableEast">East</button>
    <br>
    <ul>
          <li
            v-for="county in selectedKingdom.counties"
            :key="county.id"
          >
            {{ county.name }} led by {{ county.title }} {{ county.leader }}
            with {{ county.land }} acres
          </li>
    </ul>
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
      user: {},
      county: {},
      kingdom: {},
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
          this.kingdom = kingdom
          this.kingdomIndex = this.kingdoms.findIndex((k) => k.id === this.kingdom.id)
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
