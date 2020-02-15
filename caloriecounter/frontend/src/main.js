import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import VueCtkDateTimePicker from 'vue-ctk-date-time-picker';
import 'vue-ctk-date-time-picker/dist/vue-ctk-date-time-picker.css';
import VueMq from 'vue-mq';

import '@/services/interceptor.js'; // Interceptors are initialized with this import

Vue.component('VueCtkDateTimePicker', VueCtkDateTimePicker);

Vue.config.productionTip = false

Vue.use(VueMq, {
  breakpoints: {
    mobile: 450,
    tablet: 900,
    laptop: 1250,
    desktop: Infinity,
  }
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

