<script>
// an example array of items to be paged
import axios from 'axios';
const dataItems = axios
  .get("http://localhost:8081/api/aluno")
  .then((res) => {
          console.log(res.data)
  })
  .catch((error) => {
          console.log(error);
  });
  
console.log(dataItems);

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
<template>
    <div class="card text-center m-3">
        <h3 class="card-header">Paginação Aluno</h3>
        <div class="card-body">
            <div v-for="item in pageOfItems" :key="item.nome">{{item.email}}</div>
        </div>
        <div class="card-footer pb-0 pt-3">
            <jw-pagination :items="dataItems.nome" @changePage="onChangePage"></jw-pagination>
        </div>
    </div>
</template>
