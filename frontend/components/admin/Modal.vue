<script setup lang="ts">
defineProps<{
  show: boolean
  title: string
  confirmText?: string
  cancelText?: string
  danger?: boolean
}>()

const emit = defineEmits<{
  (e: 'confirm'): void
  (e: 'cancel'): void
}>()
</script>

<template>
  <Teleport to="body">
    <Transition name="modal">
      <div v-if="show" class="fixed inset-0 z-50 flex items-center justify-center p-4">
        <div class="absolute inset-0 bg-black/70 backdrop-blur-sm" @click="$emit('cancel')" />
        <div class="relative glass-card p-6 w-full max-w-md">
          <h3 class="text-lg font-semibold text-white mb-4">{{ title }}</h3>
          <div class="mb-6">
            <slot />
          </div>
          <div class="flex justify-end gap-3">
            <button
              class="px-4 py-2 rounded-xl text-sm font-medium text-gray-400 hover:text-white hover:bg-white/10 transition-colors"
              @click="$emit('cancel')"
            >
              {{ cancelText || 'Bekor qilish' }}
            </button>
            <button
              :class="[
                'px-4 py-2 rounded-xl text-sm font-medium text-white transition-colors',
                danger
                  ? 'bg-red-500/20 border border-red-500/50 hover:bg-red-500/30'
                  : 'bg-purple-500/20 border border-purple-500/50 hover:bg-purple-500/30',
              ]"
              @click="$emit('confirm')"
            >
              {{ confirmText || 'Tasdiqlash' }}
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.2s ease;
}
.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}
</style>
