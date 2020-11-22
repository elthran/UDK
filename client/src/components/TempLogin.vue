<template>
  <div v-if="!loading">
    You are not logged in.
    To login, please type in a valid username and password.
    To create an account, please type in a new username and password.
    <br><br>
    Username: <input>
    <br><br>
    <button @click="loginUser">Login</button> <button @click="createUser">Create Account</button>
    <br><br>Put error response here:
  </div>
</template>

<script>
import http from "@/http-client";
import systemApi from "@/api/system-api";
import countyApi from "@/api/counties-api";

export default {
  name: 'TempLogin',
  data () {
    return {
      loading: false,
    }
  },
  methods: {
    loginUser () {
      return systemApi.currentUser().then(({ user }) => {
        if (!user.id) {
          this.$router.push('/authentication/login')
          return
        }
        this.user = user
        return countyApi.fetch(user.countyId).then(({ county }) => {
          this.county = county
        })
        .catch((response) => console.log('response', response))
      })
      .catch((response) => console.log('response', response))
    },
    createUser () {
      http.get(`/api/authentication/create`)
      .then(() => {
        console.debug('Succesfully created user')
        return 'hello'
      })
      .catch((response) => console.log('response', response))
    }
  },
}
</script>

<style scoped></style>
