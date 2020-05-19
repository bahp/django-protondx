import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            redirect: '/manage0'
        },
        {
            path: '/manage0',
            name: 'layout',
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
             component: () => import(/* webpackChunkName: "about" */ './views/manage0/manage0.vue')
		},
		{
		    path: '/manage1',
		    name: 'layout',
		    // route level code-splitting
		    // this generates a separate chunk (about.[hash].js) for this route
		     component: () => import(/* webpackChunkName: "about" */ './views/manage1/manage1.vue')
		},

		 {
		     path: '/manage2',
		    name: 'layout',
		     // route level code-splitting
		     // this generates a separate chunk (about.[hash].js) for this route
		      component: () => import(/* webpackChunkName: "about" */ './views/manage2/manage2.vue')
		 }
    ]
})
