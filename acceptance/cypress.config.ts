import { defineConfig } from 'cypress'

export default defineConfig({
    e2e: {
        viewportWidth: 1400,
        viewportHeight: 1000,
        requestTimeout: 7000,
        video: false,
        retries: {
            runMode: 2,
            openMode: 0
        }
    }
})
