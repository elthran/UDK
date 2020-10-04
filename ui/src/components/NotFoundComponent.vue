<template lang="pug">
  #not-found-component
    p 404 - Page not found.
    br
    | Return to #[a(href="/") home]
</template>

<script>
export default {
  name: 'NotFoundComponent',
  mounted () {},
}
</script>

<style lang="scss" scoped>
#not-found-component {
  position: absolute;
  top: 33%;
  left: 50%;
  transform: translate(-50%, -50%);

  font-size: 1.5em;
  text-align: center;
}
</style>
