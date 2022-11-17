<template>
    <div class="card text-center m-3">
        <h3 class="card-header">Vue.js Paginação Aluno</h3>
        <div class="card-body">
            <div v-for="item in pageOfItems" :key="item.id">{{item.name}}</div>
        </div>
        <div class="card-footer pb-0 pt-3">
            <jw-pagination :items="dataItems.nome" @changePage="onChangePage"></jw-pagination>
        </div>
    </div>
</template>

<script>
// an example array of items to be paged
const dataItems =     axios
      .get('http://127.0.0.1:8000/api/alunos')
      .then(response => (this.info = response.data));

export default {
    data() {
        return {
            dataItems,
            pageOfItems: []
        };
    },
    methods: {
        onChangePage(pageOfItems) {
            // update page of items
            this.pageOfItems = pageOfItems;
        }
    }
};
</script>
