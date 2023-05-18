<template>
  <div id="app">
      <NavBar v-if="loginType.type !== 'admin' && loginType.type !== 'teacher'" />
      <NavbarTeacher v-else-if="loginType.type === 'teacher'"/>
      <NavbarAdmin v-else/>
    <!-- <img alt="Vue logo" src="./assets/logo.png">
    <HomePage msg="Welcome to Your Vue.js App"/> -->
     <router-view></router-view>   
  </div>
</template>

<script>
import NavBar from './components/Navbar/NavBar.vue'
import NavbarAdmin from './components/Navbar/NavbarAdmin.vue';
import NavbarTeacher from './components/Navbar/NavbarTeacher.vue';

export default {
  name: 'App',
  components: {
    NavBar,
    NavbarAdmin,
    NavbarTeacher
  },
  data() {
    return {
      loginType: ''
    };
  },
  mounted() {
    this.loginType = this.$cookies.get('isLoggedIn');
    if (this.loginType == null)
    {this.loginType = 'viewer'}
    console.warn(this.loginType)
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
