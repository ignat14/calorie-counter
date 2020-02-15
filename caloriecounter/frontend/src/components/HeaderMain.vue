<template>
  <div class="header-main">

    <div v-if="is_mobile" class="hamburger">
      <i class="fas fa-bars" @click="toggleLeftMenu(true)"></i>
    </div>

    <h1>Calorie Counter</h1>

    <mq-layout mq="laptop+">
      <span class="welcome-user" @click="account_menu_open = !account_menu_open">
          Welcome <b>{{ logged_user.email }}</b>
          <span class="dropdown-btn">
            <i v-if="!account_menu_open" class="fas fa-chevron-down"></i>
            <i v-if="account_menu_open" class="fas fa-chevron-up"></i>
          </span>
        <div v-if="account_menu_open" class="dropdown">
          <div class="dropdown-item">
            Change Password
          </div>
          <div class="dropdown-item" @click="logout_user">
            Logout
          </div>
        </div>
      </span>
    </mq-layout>
    
    <div v-if="is_mobile" class="welcome-user-mobile">
      <i class="fas fa-user" @click="toggleRightMenu(true)"></i>
    </div>

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
  computed: {
    ...mapGetters(["logged_user"]),
    is_mobile: function() {
      return this.$mq === 'mobile' || this.$mq === 'tablet'
    }
  },
  methods: {
    ...mapActions(['logout', 'toggleLeftMenu', 'toggleRightMenu']),
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
  align-items: center;
  border-bottom: 1px gray solid;
  background: #fff;
  position: sticky;
  top: 0;
  left: 0;
  /* width: 100%; */
  z-index: 5;
}

.header-main h1 {
  margin: 10px;
  font-family: 'Dancing Script', cursive;
}

.welcome-user {
  margin: 10px;
  padding: 0 20px;
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

.welcome-user-mobile {
  margin: 10px;
  padding: 0 10px;
}

.welcome-user-mobile i {
  cursor: pointer;
  font-size: 20px;
}

.hamburger {
  margin: 10px;
  padding: 0 10px;
}

.hamburger i {
  cursor: pointer;
  font-size: 20px;
}

</style>
