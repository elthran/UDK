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
          <td><a href="#"><strike>Kingdom</strike></a></td>
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
          <td><a href="#"><strike>War</strike></a></td>
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
      </table>
    </nav>
  </div>
</template>

<script>

</script>

<style scoped>

body {
  background-color: rgba(220, 186, 96, 1.0);
}

div.nav-bar {
  flex-basis: 400;
  flex-shrink: 0;

  margin: 20px;
  padding: 10px 10px 10px 10px;
  border: 3px solid rgba(139, 18, 59, 1);
  border-radius: 5px;

  background-color: rgba(251, 246, 224, 1);
}

a {
  font-size: large;
}

div.content {
  max-width: 800;
  margin: 20px;
  border-style: solid;
  border-width: 3px;
  border-radius: 5px;
  border-color: rgba(139, 18, 59, 1);
  background-color: rgba(251, 246, 224, 1);
}

div.data-block {
  flex-basis: 600px;
  flex-grow: 1;
  flex-shrink: 1;
  margin: 5px;
  padding: 10px;
  border: 3px solid rgba(139, 18, 59, 1);
}

a:link, visited, hover, active {
  text-decoration: none;
  color: rgba(4, 56, 93, 1);
}

a:visited {
  text-decoration: none;
  color: rgba(4, 56, 93, 1);
}

a:hover {
  text-decoration: none;
  color: rgba(4, 56, 93, 1);
}

a:active {
  text-decoration: none;
  color: rgba(4, 56, 93, 1);
}

.page {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
}

.page table {
  margin: 5px;
}

div.nav-bar table tr td {
  padding-top: 3px;
  padding-bottom: 3px;
}

.flex-container {
  display: flex;
  flex-direction: column
}

.flex-container-2 {
  display: flex;
  flex-direction: row;
}

h3 {
  font-size: medium;
  font-weight: bold;
  text-align: left;
}

table.infrastructure tr td, th {
  border: 1px solid black;
  padding: 5px 5px 5px 5px;
}

table.odd {
}

table.odd tr td, th {
  border: 1px solid #ccc;
  padding: 5px;
}

table.odd tr:nth-child(2n+1) {
  background: #f1f1f1;
}

table.people tr td, th {
  border: 1px solid #000000;
  padding: 5px 5px 5px 5px;
}

.value-cell {
  text-align: center;
}

</style>
