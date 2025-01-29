<template>
    <div>
        <p>Вы уверены, что хотите выйти?</p>
        <button @click="logout">Выйти</button>
    </div>
</template>

<script>

export default {
    logout() {
        this.$store.dispatch('logout')
        this.$router.push('/login') // Перенаправление на страницу входа
    },
}
</script>

<style></style>