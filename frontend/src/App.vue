<template>
	<HeaderBar></HeaderBar>
	<BodyComponent :menu-option="this.menuOption"></BodyComponent>
	<NavBar :menu-option="this.menuOption"></NavBar>
<!--	<MainScreen/>-->
</template>

<script>
import HeaderBar from "@/layout/Header";
import BodyComponent from "@/layout/BodyComponent";
import NavBar from "@/layout/NavBar";

export default {
	name: 'App',
	components: {
		NavBar,
		BodyComponent,
		HeaderBar
	},
	data() {
		return {
			menuOption: 0
		}
	}
}
</script>

<style>
* {
	margin: 0;
	padding: 0;
}

body {
	background-color: #fffaf0;
}
</style>
