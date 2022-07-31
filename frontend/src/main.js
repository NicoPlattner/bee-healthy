import {createApp} from 'vue'
import BootstrapVue3 from 'bootstrap-vue-3'
import {BootstrapIconsPlugin} from "bootstrap-icons-vue";

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import App from "@/App";
import {Weather} from "@/enums/weather.enum";

import mitt from 'mitt';
const emitter = mitt();

const app = createApp(App)
app.config.globalProperties.emitter = emitter;
app.use(BootstrapVue3)
app.use(BootstrapIconsPlugin)
app.use(Weather)
app.mount('#app')
