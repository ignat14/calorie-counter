<template>
  <div class="header-main">
    <h1>Calorie Counter</h1>
    <span class="welcome-user" @click="account_menu_open = !account_menu_open">
      Welcome <b>{{ logged_user.email }}</b>
      <span class="dropdown-btn">
        <i v-if="!account_menu_open" class="fas fa-chevron-down"></i>
        <i v-if="account_menu_open" class="fas fa-chevron-up"></i>
      </span>
      <div v-if="account_menu_open" class="dropdown">
        <div class="dropdown-item">
          Settings
        </div>
        <div class="dropdown-item" @click="logout_user">
          Logout
        </div>
      </div>
    </span>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: 'HeaderMain',
  data() {
		return {
			account_menu_open: false
		};
	},
  computed: mapGetters(["logged_user"]),
  methods: {
    ...mapActions(['logout']),
    logout_user: function() {
      this.logout();
    }
  }
}
</script>


<style scoped>

.header-main {
  display: flex;
  justify-content: space-between;
  border-bottom: 1px gray solid;
  background: #fff;
  position: fixed;
  padding-bottom: 1px;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 50;
}

.header-main h1 {
  margin: 10px;
  font-family: 'Dancing Script', cursive;
  padding: 0 30px;
}

.welcome-user {
  margin: 20px;
  padding: 0 30px;
  position: relative;
  cursor: pointer;
}

.dropdown-btn {
  position: relative;
  margin-left: 10px;
  cursor: pointer;
}

.dropdown {
  position: absolute;
  top: 100%;
  left: 50%;
  width: 100%;
  height: 50px;
  background: white;
  transform: translate(-50%, 20px);
}

.dropdown-item {
  padding: 10px;
  border: 1px gray solid;
  background: white;
}

.dropdown-item:hover {
  background: var(--main-blue);
  color: white;
}

</style>
