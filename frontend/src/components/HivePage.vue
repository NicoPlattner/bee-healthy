<template>
  <div>
    <b-row style="height: 3em">
      <b-col cols="4">
        <div class='square-box'>
          <div class='square-content'>
            <div style="padding: .3em; text-align: center">
              <i  v-if="this.weather === 0"  class="bi bi-sun"></i>
              <i  v-if="this.weather === 1"  class="bi bi-cloud-sun"></i>
              <i  v-if="this.weather === 2"  class="bi bi-clouds"></i>
              <i  v-if="this.weather === 3"  class="bi bi-cloud-drizzle"></i>
              <i  v-if="this.weather === 4"  class="bi bi-cloud-rain-heavy"></i>
              <i  v-if="this.weather === 5"  class="bi bi-cloud-lightning"></i>
              <i  v-if="this.weather === 6"  class="bi bi-cloud-snow"></i>
            </div>
          </div>
        </div>
      </b-col>

      <b-col cols="8">
        <div class='rect-box'>
          <div class='square-content'>
            <div class="app-content">
              {{ this.temperature }}°C
            </div>
          </div>
        </div>

      </b-col>
    </b-row>

  </div>
</template>

<script>
import {Weather} from "@/enums/weather.enum";

export default {
  name: "HivePage",
  data() {
    return {
      selected: 'All Hives',
      temperature: 0,
      weather: Weather.Sunny
    }
  },
  mounted() {
    this.temperature = 36;
    this.weather = Weather.LightClouds;

    fetch('http://localhost:5000/getAllHives/0')
        .then((response) => response.json())
        .then((data) => console.log(data));
  }
}
</script>

<style scoped>

.app-content {
  margin-top: .3em;
  text-align: center;
}

.square-box{
  position: relative;
  overflow: hidden;
  width: 100%;
  margin-right: 10%;
  background: #FFCD32;
  border-radius: .7em;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}

.rect-box {
  position: relative;
  overflow: hidden;
  width: 100%;
  margin-right: 10%;
  background: #FFCD32;
  border-radius: .7em;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}

.square-box:before{
  content: "";
  display: block;
  padding-top: 100%;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}

.rect-box:before{
  content: "";
  display: block;
  padding-top: 45%;
  color: black;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}

.square-content{
  position:  absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  color: black;
  font-size: 2.5em;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}

</style>