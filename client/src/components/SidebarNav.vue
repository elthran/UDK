<template>
  <div v-if="!loading">
    <div class="page">
      <nav name="" class="nav-bar">
        <h3>Overview</h3>

        <table>
          <tr>
            <td><router-link :to="{ name: 'county.home' }">County Home</router-link></td>
          </tr>
          <tr>
            <td>
              <a href="#"><strike>Kingdom</strike></a>
            </td>
          </tr>
        </table>

        <h3>Advisors</h3>

        <table>
          <tr>
            <td><router-link :to="{ name: 'county.economy' }">Economics</router-link></td>
          </tr>
          <tr>
            <td><router-link :to="{ name: 'county.infrastructure' }">City Planner</router-link></td>
          </tr>
          <tr>
            <td>
              <a href="#"><strike>War</strike></a>
            </td>
          </tr>
          <tr>
            <td>
              <a href="#"><strike>Thieves Guild</strike></a>
            </td>
          </tr>
          <tr>
            <td>
              <a href="#"><strike>Wizard Council</strike></a>
            </td>
          </tr>
          <tr>
            <td>
              <a href="#"><strike>Scientist</strike></a>
            </td>
          </tr>
        </table>

        <h3>Diplomacy</h3>

        <table>
          <tr>
            <td>
              <a href="#"><strike>Town Hall</strike></a>
            </td>
          </tr>
          <tr>
            <td>
              <a href="#"><strike>Messages</strike></a>
            </td>
          </tr>
          <tr>
            <td>
              <a href="#"><strike>Trade</strike></a>
            </td>
          </tr>
          <tr>
            <td>
              <a href="#"><strike>Allegiances</strike></a>
            </td>
          </tr>
        </table>

        <h3>About the Game</h3>

        <table>
          <tr>
            <td>
              <a href="#"><strike>Achievements</strike></a>
            </td>
          </tr>
          <tr>
            <td>
              <a href="#"><strike>Leaderboard</strike></a>
            </td>
          </tr>
          <tr>
            <td>
              <a href="#"><strike>Player Guide</strike></a>
            </td>
          </tr>
          <tr>
            <td>
              <a href="#"><strike>Forums</strike></a>
            </td>
          </tr>
          <tr>
            <td>
              <a href="#"><strike>Credits</strike></a>
            </td>
          </tr>
        </table>
      </nav>
    </div>
  </div>
</template>

<script>

</script>

<style scoped>

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

</style>
