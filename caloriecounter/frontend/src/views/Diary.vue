<template>
  <div class="home">
    <MyMealsList />
  </div>
</template>

<script>
import MyMealsList from '@/components/my_meals/MyMealsList.vue';

export default {
  name: 'Diary',
  components: {
    MyMealsList
  }
}
</script>
