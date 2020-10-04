<template lang="pug">
  #app
    #nav
      router-link(to="/")
        | Home |
      router-link(to="/county/home")
        |
        | County Home
    router-view
</template>

<script>
export default {
  name: 'App',
  components: {},
  data () {
    return {
      isLoading: true,
    }
  },
  watch: {
    $route (to, from) {
      this.isLoading = true
      this.$emit('refocus')
      this.$nextTick(() => {
        this.focusTop()
      })
    },
  },
  methods: {
    focusTop () {
      window.scrollTo(0, 0)
    },
  },
}
</script>

<style lang="scss" scoped>
@media (max-width: 640px) {
  #app {
    display: flex;
    flex-direction: column;
  }
}

@media (min-width: 640px) {
  #app {
    display: flex;
    flex-direction: row-reverse;
    justify-content: flex-end;
  }
}
</style>
