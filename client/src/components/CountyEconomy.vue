<template>
  <div v-if="!loading">
    <table>
      <tr>
        <th style="width:50px;">Topic</th>
        <th style="width:50px;">Current</th>
        <th style="width:75px;">Projected Change</th>
        <th style="width:200px;">Modifiers</th>
        <th style="width:180px;">Projected Growth</th>
        <th style="width:180px;">Projected Losses</th>
        <th style="width:225px;">Notes</th>
      </tr>
      <tr>
        <td>Population</td>
        <td>{{ county.population }}</td>
        <td>Change?</td>
        <td>Modifiers?</td>
        <td>
          <ul>
            <li>Births:</li>
            <li>Immigration:</li>
          </ul>
        </td>
        <td>
          <ul>
            <li>Deaths: ?</li>
            <li>Emigration: ?</li>
          </ul>
        </td>
        <td>Your basic birth rate is based on your total land.
          Happiness, tax rate, and health will affect population growth.
        </td>
      </tr>
      <tr>
        <td>Gold</td>
        <td>{{ county.gold }}</td>
        <td>Change?</td>
        <td>Modifiers?</td>
        <td>
          <ul>
            <li
              v-if="preference.productionChoice === 'Overwork'"
            >Overworking: Should have some benefit...
            </li>
          </ul>
        </td>
        <td>
          <ul>
            <li>Military Expenses: ?</li>
          </ul>
        </td>
        <!-- These conditions must not occur together or it will break the table. -->
        <td
          v-if="preference.taxRate < 7"
          class="green">Your current tax rate has a positive effect on happiness.
        </td>
        <td
          v-else-if="preference.taxRate === 7"
        >Your current tax rate has no effect on happiness.
        </td>
        <td
          v-else
          class="red">Your current tax rate has a negative effect on happiness.
        </td>
      </tr>
      <tr>
        <td>Food</td>
        <td>{{ county.grainStores }}</td>
        <td>Change?</td>
        <td>
          <ul>
            <li>Rations: {{ preference.rations }}</li>
          </ul>
        </td>
        <td>
          <ul>
            <li>Fields: + grain production?</li>
            <li>Pastures: + dairy production?</li>
            <li
              v-if="preference.productionChoice === 'Foraging'"
            >Foraging: + some bonus???
            </li>
          </ul>
        </td>
        <td>
          <ul>
            <li>To be Eaten: ???</li>
          </ul>
        </td>
        <td>Excess dairy can not be stored in your granaries. If you do not have enough food,
          your populace will begin to starve.
        </td>
      </tr>
      <tr>
        <td>Lumber</td>
        <td>{{ county.wood }}</td>
        <td></td>
        <td>-</td>
        <td>?</td>
        <td>-</td>
        <td>Lumber is used to build buildings and to equip certain soldiers.</td>
      </tr>
      <tr>
        <td>Iron</td>
        <td>{{ county.iron }}</td>
        <td></td>
        <td>-</td>
        <td>?</td>
        <td>-</td>
        <td>Iron is used to equip powerful soldiers.</td>
      </tr>
      <tr>
        <td>Stone</td>
        <td>{{ county.stone }}</td>
        <td></td>
        <td>-</td>
        <td>?</td>
        <td>-</td>
        <td>Stone stone.</td>
      </tr>
      <tr>
        <td>Mana</td>
        <td>{{ county.mana }} / {{ county.maxMana }}</td>
        <td>+{{ county.manaChange }}</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>Mana is used to cast spells as well as dispel enemy magic.
          You can raise your maximum mana by researching arcane lore.
        </td>
      </tr>
      <tr>
        <td>Happiness</td>
        <td></td>
        <td></td>
        <td>-</td>
        <td></td>
        <td></td>
        <td>Happiness affects your birth rate. If they become too unhappy,
          they may start to question your rule.
        </td>
      </tr>
      <tr>
        <td>Healthiness</td>
        <td>{{ county.healthiness }}%</td>
        <td></td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>Healthiness affects your death rate. As they become more unhealthy, they die
          and get sick much more easily. Your healthiness decreases by 1% for every
          200 unfed people each day.
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import countyApi from '@/api/counties-api';
import preferenceApi from '@/api/preference-api';

export default {
  name: 'CountyEconomy',
  components: {},
  props: {},
  data() {
    return {
      user: {},
      county: {
        economy: {},
        preference: {},
      },
      loading: false,
    };
  },
  computed: {
    preference() {
      return this.county.preference;
    },
  },
  mounted() {
    this.loading = true;
    Promise.all([countyApi.fetch(1), preferenceApi.fetch(1)])
      .then(([{ county }, { preference }]) => {
        Object.assign(this.county, county);
        Object.assign(this.county.preference, preference);
      })
      .finally(() => {
        this.loading = false;
      });
  },
};
</script>

<style scoped>
</style>
