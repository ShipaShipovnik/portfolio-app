vue
Copy
<template>
    <div
        v-if="store.isVisible"
        class="toast-container position-fixed top-0 end-0 p-3"
    >
        <div
            class="toast align-items-center"
            :class="store.classes"
            role="alert"
            aria-live="assertive"
            aria-atomic="true"
        >
            <div class="d-flex">
                <div class="toast-body">
                    {{ store.message }}
                </div>
                <button
                    type="button"
                    class="btn-close me-2 m-auto"
                    data-bs-dismiss="toast"
                    aria-label="Close"
                    @click="store.isVisible = false"
                ></button>
            </div>
        </div>
    </div>
</template>

<script>
import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const store = useToastStore()

        return {
            store
        }
    }
}
</script>

<style scoped>
.toast-container {
    z-index: 1050; /* Убедитесь, что toast поверх других элементов */
}

.toast {
    transition: opacity 0.5s ease, transform 0.5s ease;
    opacity: 0;
    transform: translateY(-100%);
}

.toast.show {
    opacity: 1;
    transform: translateY(0);
}
</style>