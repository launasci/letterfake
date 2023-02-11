<template>
  <div
    cols="3"
    class="d-flex flex-row mt-16"
  >
    <v-col>
      <v-title class="ml-5 text-h6 font-weight-regular">
        Terror
      </v-title>
      <v-progress-circular
        class="ml-n2 mt-6 mb-16"
        :value="porcentagem['Terror']"
        color="blue-grey"
        :width="width"
        :size="size"
      >
        {{ Math.round(porcentagem["Terror"]) || "0" }}%
      </v-progress-circular>
    </v-col>
    <v-col>
      <v-title class="ml-5 text-h6 font-weight-regular">
        Comedia
      </v-title>
      <v-progress-circular
        class="ml-n2 mt-6 mb-16"
        :value="porcentagem['Comedia']"
        color="deep-orange lighten-2"
        :width="width"
        :size="size"
      >
        {{ Math.round(porcentagem["Comedia"]) || "0" }}%
      </v-progress-circular>
    </v-col>

    <v-col>
      <v-title class="ml-5 text-h6 font-weight-regular">
        Ação
      </v-title>
      <v-progress-circular
        class="ml-n2 mt-6 mb-16"
        :value="porcentagem['Ação']"
        color="brown"
        :width="width"
        :size="size"
      >
        {{ Math.round(porcentagem["Ação"]) || "0" }}%
      </v-progress-circular>
    </v-col>

    <v-col>
      <v-title class="ml-5 text-h6 font-weight-regular">
        Drama
      </v-title>
      <v-progress-circular
        class="ml-n2 mt-6 mb-16"
        :value="porcentagem['Drama']"
        color="lime"
        :width="width"
        :size="size"
      >
        {{ Math.round(porcentagem["Drama"]) || "0" }}%
      </v-progress-circular>
    </v-col>

    <v-col>
      <v-title class="ml-5 text-h6 font-weight-regular">
        Outros
      </v-title>
      <v-progress-circular
        class="ml-n2 mt-6 mb-16"
        :value="porcentagem['Outros']"
        color="indigo darken-2"
        :width="width"
        :size="size"
      >
        {{ Math.round(porcentagem["Outros"]) || "0" }}%
      </v-progress-circular>
    </v-col>
  </div>
</template>

<script>
export default {
  props: ["porcentagem"],

  data: () => {
    return {
      size: 130,
      width: 6,
    };
  },
};
</script>

<style scoped></style>
