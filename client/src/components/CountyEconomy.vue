<template>
  <div v-if="!loading">
    <div class="content flex-container">
      <div class="flex-container-2" style="order: 1">
        <div class="data-block" style="order: 0;">
          <p>DATA 1</p>
          <table class="people">
            <tr>
              <th>Population</th>
              <th>Happiness</th>
              <th>Healthiness</th>
            </tr>
            <tr>
              <td>
                <img src="@/assets/images/person.jpeg" width="100" height="100" alt="person_icon">
              </td>
              <td>
                <img src="@/assets/images/smiley.jpeg" width="100" height="100" alt="smile_icon">
              </td>
              <td>
                <img src="@/assets/images/heart.jpeg" width="100" height="100" alt="heart_icon">
              </td>
            </tr>
            <tr>
              <td class="value-cell">{{ county.population }}</td>
              <td class="value-cell">{{ county.happiness }}%</td>
              <td class="value-cell">{{ county.healthiness }}%</td>
            </tr>
          </table>
        </div>
      </div>
      <div
        style="margin: 5px; min-width: 600; order: 2; padding: 5px 5px 5px 5px;
        border: 3px solid rgba(139, 18, 59, 1);">
        <table class="odd">
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
                  v-if="county.productionChoice === 'Overwork'"
                >Overworking: Should have some benefit...
                </li>
              </ul>
            </td>
            <td>
              <ul>
                <li>Military Expenses: ?</li>
              </ul>
            </td>
            <td
              v-if="county.taxRate < 7"
              class="green">Your current tax rate has a positive effect on happiness.
            </td>
            <td
              v-else-if="county.taxRate === 7"
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
                <li>Rations: {{ county.rations }}</li>
              </ul>
            </td>
            <td>
              <ul>
                <li>Fields: + grain production?</li>
                <li>Pastures: + dairy production?</li>
                <li>If Foraging: + some bonus???</li>
              </ul>
            </td>
            <td>
              <ul>
                <li>To be Eaten: ???</li>
              </ul>
            </td>
            <td>Excess dairy can not be stored in your granaries.
              If you do not have enough food, your populace will begin to starve.
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
            <td>{{ county.happiness }}%</td>
            <td>{{ county.happinessChange }}</td>
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
            <td>Healthiness affects your death rate. As they become more unhealthy,
              they die and get sick much more easily.
              Your healthiness decreases by 1% for every 200 unfed people each day.
            </td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import countyApi from '@/api/counties-api';

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
  mounted() {
    this.loading = true;
    Promise.all([countyApi.fetch(1)])
      .then(([{ county }]) => {
        Object.assign(this.county, county);
      })
      .finally(() => {
        this.loading = false;
      });
  },
};
</script>

<style scoped>
</style>
