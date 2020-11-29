<template>
  <div v-if="!loading">
    <nav name="" class="nav-bar">
      <h3>Overview</h3>
      <table>
        <tr>
          <td>
            <router-link :to="{ name: 'county.home' }">County</router-link>
          </td>
        </tr>
        <tr>
          <td>
            <router-link :to="{ name: 'kingdom' }">Kingdom</router-link>
          </td>
        </tr>
      </table>
      <h3>Advisors</h3>
      <table>
        <tr>
          <td>
            <router-link :to="{ name: 'county.economy' }">Economics</router-link>
          </td>
        </tr>
        <tr>
          <td>
            <router-link :to="{ name: 'county.infrastructure' }">City Planner</router-link>
          </td>
        </tr>
        <tr>
          <router-link :to="{ name: 'county.military' }">War</router-link>
        </tr>
        <tr>
          <td><a href="#"><strike>Thieves Guild</strike></a></td>
        </tr>
        <tr>
          <td><a href="#"><strike>Wizard Council</strike></a></td>
        </tr>
        <tr>
          <td><a href="#"><strike>Scientist</strike></a></td>
        </tr>
      </table>
      <h3>Diplomacy</h3>
      <table>
        <tr>
          <td><a href="#"><strike>Town Hall</strike></a></td>
        </tr>
        <tr>
          <td><a href="#"><strike>Messages</strike></a></td>
        </tr>
        <tr>
          <td><a href="#"><strike>Trade</strike></a></td>
        </tr>
        <tr>
          <td><a href="#"><strike>Allegiances</strike></a></td>
        </tr>
      </table>
      <h3>About the Game</h3>
      <table>
        <tr>
          <td><a href="#"><strike>Achievements</strike></a></td>
        </tr>
        <tr>
          <td><a href="#"><strike>Leaderboard</strike></a></td>
        </tr>
        <tr>
          <td><a href="#"><strike>Player Guide</strike></a></td>
        </tr>
        <tr>
          <td><a href="#"><strike>Forums</strike></a></td>
        </tr>
        <tr>
          <td><a href="#"><strike>Credits</strike></a></td>
        </tr>
        <tr>
          <td><button @click="logoutCurrentUser">Logout</button></td>
        </tr>
      </table>
    </nav>
  </div>
</template>

<script>
import authenticationApi from "@/api/authentication-api";

export default {
  name: 'SidebarNav',
  data () {
    return {
      loading: false,
    }
  },
  methods: {
    logoutCurrentUser () {
      authenticationApi.logout()
      .then(({ message }) => {
        window.localStorage.removeItem('currentUserId')
        console.debug(message)
        this.$router.push({ name: 'authentication.login' })
      })
      .catch((error) => console.log('error', error))
    }
  },
}
</script>

<style scoped></style>
