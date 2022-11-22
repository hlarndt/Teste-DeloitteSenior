<script>
import { defineAsyncComponent } from "vue";

const exampleItems = [...Array(300).keys()].map(i => ({ id: (i+1), name: 'Item ' + (i+1) }));

const dataItems = {};

export default {
    async asyncData ({ $axios }) {
        const user = 'admin';
        const password = '060174';

        const dataItems = await $axios.post(
            'http://127.0.0.1:8081/login/',
            {
                'username': user,
                'password': password
            },
            {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }
            }
        );
        console.log(dataItems);
        return { dataItems }
    }, 
    data() {
        return {
            exampleItems,
            dataItems,
            pageOfItems: []
        };
    },
    methods: {
        onChangePage(pageOfItems) {
            this.pageOfItems = pageOfItems;
        }
    }
};
</script>
<template>
    <div class="card text-center m-3">
        <h3 class="card-header">Paginação Aluno</h3>
        <div class="card-body">
            <div v-for="item in pageOfItems" :key="item.id">{{item.name}}</div>
        </div>
        <div class="card-footer pb-0 pt-3">
            <jw-pagination :items="exampleItems" @changePage="onChangePage" :pageSize="30"></jw-pagination>
        </div>
    </div>
</template>
