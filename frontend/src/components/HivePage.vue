<template>
	<div>
		<b-row style="height: 3em; margin-bottom: 4em">
			<b-col cols="4">
				<div class='square-box'>
					<div style="background-color: green" class='square-content' v-if="this.hive.sensorData.predictedHealthStatus[this.hive.sensorData.predictedHealthStatus.length - 1] > 70">
						<div class="app-content">
							<i class="bi bi-check-lg"></i>
						</div>
					</div>
					<div style="background-color: #FFCD32" class='square-content' v-if="this.hive.sensorData.predictedHealthStatus[this.hive.sensorData.predictedHealthStatus.length - 1] <= 70 && this.hive.sensorData.predictedHealthStatus[this.hive.sensorData.predictedHealthStatus.length - 1] > 50 ">
						<div class="app-content">
							<i class="bi bi-info-circle"></i>
						</div>
					</div>
					<div style="background-color: orangered" class='square-content' v-if="this.hive.sensorData.predictedHealthStatus[this.hive.sensorData.predictedHealthStatus.length - 1] <= 50 ">
						<div class="app-content">
							<i class="bi bi-exclamation-lg"></i>
						</div>
					</div>
				</div>
			</b-col>
			<b-col cols="8">
				<div class='rect-box'>
					<div class='square-content'>
						<div class="app-content">
							{{ this.hive.sensorData.weight[this.hive.sensorData.weight.length - 1] }} kg
						</div>
					</div>
				</div>
			</b-col>
		</b-row>
		<b-row style="height: 3em; margin-bottom: 4.1em">
			<b-col cols="8">
				<div class='rect-box'>
					<div class='square-content'>
						<div class="app-content">
							<i class="bi bi-thermometer-half"></i>
							{{ this.hive.sensorData.temperature[this.hive.sensorData.temperature.length - 1] }}°C
						</div>
					</div>
				</div>
			</b-col>
			<b-col cols="4">
				<div class='square-box'>
					<div class='square-content'>
						<div style="padding: .3em; text-align: center">
							<i v-if="this.hive.sensorData.weather[this.hive.sensorData.weather.length - 1] === 0" class="bi bi-sun"></i>
							<i v-if="this.hive.sensorData.weather[this.hive.sensorData.weather.length - 1] === 1" class="bi bi-cloud-sun"></i>
							<i v-if="this.hive.sensorData.weather[this.hive.sensorData.weather.length - 1] === 2" class="bi bi-clouds"></i>
							<i v-if="this.hive.sensorData.weather[this.hive.sensorData.weather.length - 1] === 3" class="bi bi-cloud-drizzle"></i>
							<i v-if="this.hive.sensorData.weather[this.hive.sensorData.weather.length - 1] === 4" class="bi bi-cloud-rain-heavy"></i>
							<i v-if="this.hive.sensorData.weather[this.hive.sensorData.weather.length - 1] === 5" class="bi bi-cloud-lightning"></i>
							<i v-if="this.hive.sensorData.weather[this.hive.sensorData.weather.length - 1] === 6" class="bi bi-cloud-snow"></i>
						</div>
					</div>
				</div>
			</b-col>
		</b-row>
		<b-row style="height: 3em; margin-bottom: 4em">
			<b-col cols="12">
				<div class='flat-box'>
					<div class='square-content'>
						<div class="app-content-small">
							Type: <br>
							<b>{{ this.hive.beeType }}</b>
						</div>
					</div>
				</div>
			</b-col>
		</b-row>
		<b-row style="height: 6em; margin-bottom: 4em">
			<b-col cols="12">
				<div class='flat-box-double'>
					<div class='square-content'>
						<div class="app-content-small">
							<b>Sensordata:</b><br>
							Humidity: {{ this.hive.sensorData.humidity[this.hive.sensorData.humidity.length - 1] }}% <br>
							Pressure: {{ this.hive.sensorData.pressure[this.hive.sensorData.pressure.length - 1] /10 }} mbar <br>
							Volume: {{ this.hive.sensorData.beeSoundVolume[this.hive.sensorData.beeSoundVolume.length - 1] }}dB <br>
							Air Quality: {{ this.hive.sensorData.airQuality[this.hive.sensorData.airQuality.length - 1] }}% <br>

						</div>
					</div>
				</div>
			</b-col>
		</b-row>
	</div>
</template>

<script>
export default {
	name: "HivePage",
	props: {
		hive: {}
	}
}
</script>

<style scoped>

.app-content {
	margin-top: .3em;
	text-align: center;
}

.app-content-small {
	margin-top: .3em;
	margin-left: .5em;
	font-size: .63em;
}

.square-box {
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

.flat-box {
	position: relative;
	overflow: hidden;
	width: 100%;
	margin-right: 10%;
	background: #FFCD32;
	border-radius: .7em;
	box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}

.flat-box-double {
	position: relative;
	overflow: hidden;
	width: 100%;
	margin-right: 10%;
	background: #FFCD32;
	border-radius: .7em;
	box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}

.square-box:before {
	content: "";
	display: block;
	padding-top: 100%;
	box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}

.rect-box:before {
	content: "";
	display: block;
	padding-top: 45%;
	color: black;
	box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}

.flat-box:before {
	content: "";
	display: block;
	padding-top: 29%;
	color: black;
	box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}

.flat-box-double:before {
	content: "";
	display: block;
	padding-top: 63%;
	color: black;
	box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}

.square-content {
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	color: black;
	font-size: 2.5em;
	box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}

</style>
