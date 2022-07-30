<template>
  <div>
    <HeaderBar></HeaderBar>
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-1-square-fill" viewBox="0 0 16 16">
      <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2Zm7.283 4.002V12H7.971V5.338h-.065L6.072 6.656V5.385l1.899-1.383h1.312Z"/>
    </svg>

    <div id="bodycontent">
      <b-container>
        <b-row>
          <form>
            <div class="form-group">
              <label for="exampleFormControlSelect1"></label>
              <select class="form-control" id="exampleFormControlSelect1">
                <option>All Hives</option>
                <option>Beehive 1</option>
                <option>Beehive 2</option>
                <option>Beehive 3</option>
              </select>
            </div>
          </form>
        </b-row>
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
      </b-container>
    </div>
  </div>

</template>

<script>
import HeaderBar from "@/layout/Header";
import {Weather} from "@/enums/weather.enum";
export default {
  name: "MainScreen",
  components: {HeaderBar},
  data() {
    return {
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
#bodycontent {
  padding: 0 2em;
}

.app-content {
  margin-top: .3em;
  text-align: center;
}

select {
  box-shadow: rgba(17, 17, 26, 0.1) 0px 0px 16px;
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

.row {
  margin-bottom: 2em;
}

</style>