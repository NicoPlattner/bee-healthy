<template>
	<div>
		<HeaderBar></HeaderBar>

		<div id="bodycontent">
			<b-container>
				<b-row>
					<form>
						<div class="form-group">
							<label for="exampleFormControlSelect1"></label>
							<select v-model="selected" class="form-control" id="exampleFormControlSelect1" v-if="hives.length > 0">
								<option>All Hives</option>
								<option v-for="hive in this.hives" v-bind:key="hive.id">
									{{ hive.name }}
								</option>
							</select>
						</div>
					</form>
				</b-row>

				<OverviewPage v-if="this.selected === 'All Hives'"></OverviewPage>
				<HivePage v-if="this.selected !== 'All Hives'"></HivePage>
			</b-container>
		</div>
	</div>
</template>

<script>
import HeaderBar from "@/layout/Header";
import {Weather} from "@/enums/weather.enum";
import OverviewPage from "@/components/OverviewPage";
import HivePage from "@/components/HivePage";

export default {
	name: "MainScreen",
	components: {HivePage, OverviewPage, HeaderBar},
	data() {
		return {
			selected: 'All Hives',
			hives: [],
			temperature: 0,
			weather: Weather.Sunny
		}
	},
	mounted() {
		this.temperature = 36;
		this.weather = Weather.LightClouds;

		fetch('http://localhost:5000/getAllHives/0')
		.then((response) => response.json())
		.then((data) => this.hives = data);
	}
}
</script>

<style scoped>
#bodycontent {
	padding: 0 2em;
}

select {
	box-shadow: rgba(17, 17, 26, 0.1) 0px 0px 16px;
}


.row {
	margin-bottom: 2em;
}

</style>
