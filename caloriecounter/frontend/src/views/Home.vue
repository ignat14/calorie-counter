<template>
  <div class="home">
    <HeaderMain/>
    <MyMealsList/>
  </div>
</template>

<script>
// @ is an alias to /src
import HeaderMain from '@/components/HeaderMain.vue';
import MyMealsList from '@/components/MyMealsList.vue';

export default {
  name: 'Home',
  components: {
    HeaderMain,
    MyMealsList
  }
}
</script>
