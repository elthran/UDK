<template>
  <div id="app">
    <div style="height:2em;background:red;width:100%;
    text-align:center;line-height:2em;font-weight:bold;">
      RUNNING LOCALLY - NOT PRODUCTION
    </div>
    <div class="page">
      <sidebar-nav/>
      <router-view/>
    </div>
  </div>
</template>

<script>
import SidebarNav from '@/components/SidebarNav.vue';

export default {
  name: 'App',
  components: { SidebarNav },
  props: {},
  computed: {},
};
</script>

<!--
<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.page {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
}

.page table {
  margin: 5px;
}
</style>
!-->
