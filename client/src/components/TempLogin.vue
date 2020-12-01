<template>
  <div v-if="!loading">
    <div class="content flex-container">
      <div class="login-box" style="margin: 50px;">
        You are not logged in.
        <br><br>
        <p>
          To login, please type in a valid username and password.<br>
          To create an account, please type in a new username and password.
        </p>
        <br>
        <form @submit.prevent>
          <label for="username">Username: </label>
          <input
            id="username"
            type="text"
            v-model="username"
          />
          <br />
          <label for="password">Password: </label>
          <input
            id="password"
            type="password"
            v-model="password"
          />
        </form>
        <br><br>
        <button style="flex-basis: 300px; flex-shrink: false; margin: 10px;" @click="loginUser" @keyup.enter="loginUser">Login</button>
        <button style="flex-basis: 300px; flex-shrink: false; margin: 10px;" @click="createUser">Create Account</button>
        <br><br>
        <p>
          Put error response here:
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import authenticationApi from "@/api/authentication-api";
import usersApi from '@/api/users-api'

export default {
  name: 'TempLogin',
  data () {
    return {
      loading: false,
      username: null,
    }
  },
  methods: {
    loginUser () {
      return authenticationApi.login({
        username: this.username
      }).then(({ user }) => {
        console.debug('user', user)

        if (user && user.id) {
          window.localStorage.setItem('currentUserId', user.id)
          this.$router.push({ name: 'county.home' })
        }
      })
      .catch((error) => {
        console.log('error', error)
      })
    },
    createUser () {
      usersApi.create({
        username: this.username
      })
      .then(({ user }) => {
        this.username = user.username
        return this.loginUser()
      })
      .catch((response) => console.log('response', response))
    }
  },
}
</script>

<style scoped></style>
