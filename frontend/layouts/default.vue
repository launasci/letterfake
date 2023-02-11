<template>
  <v-app class="bcg">
    <v-main>
      <router-view />
    </v-main>
    <v-footer
      class="footer"
      padless
    >
      <v-col
        class="text-center"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
      </v-col>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
}
</script>
 <style>
 .bcg{
  background-color: black !important;
 }
</style>