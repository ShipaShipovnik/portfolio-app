<template>
    <div class="main-page container fill">
        <h1>Поиск</h1>
        <div class="container pt-5 row mx-auto h-75 gap-4">
            <div class="row p-3 mx-auto shadow">
                <div class="input-group rounded">
                    <input type="search" class="form-control rounded" placeholder="Search" aria-label="Search"
                        aria-describedby="search-addon" />
                    <span class="input-group-text border-0 text-warning" id="search-addon">
                        Найти
                    </span>
                </div>
            </div>
            <div class="sidebar col-4  w-25 p-3 mx-auto shadow">
                <p class="text-muted">Фильтрация:</p>
                <label class="">Цена <input type="text">р. - <input type="text"></label>
                <label for="">Категория</label><input type="text">
            </div>
            <div class="main-block p-3 col shadow">
                <p class="text-muted">Результат поиска:</p>
                <p class="text-muted">Вы еще ничего не искали):</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style></style>