module.exports = function(grunt) {

    // Project configuration
    grunt.initConfig({
	pkg: grunt.file.readJSON('package.json'),
	uglify: {
	    options: {
		banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
	    },
	    build: {
		src: 'src/js/<%= pkg.name %>.js',
		dest: 'build/js/<%= pkg.name %>.min.js'
	    }
	},
	sass: {
	    dev: {
		options: {
		    lineNumbers: true,
		    update: true,
		    trace: true,
		    style: 'expanded'
		},
		files: [{
		    expand: true,
		    cwd: 'src/sass/',
		    src: ['**/*.scss'],
		    dest: 'build/css/',
		    ext: '.css'
		}]
	    },
	    dist: {
		options: {
		    style: 'compressed'
		},
		files: [{
		    expand: true,
		    cwd: 'src/sass/',
		    src: ['**/*.scss'],
		    dest: 'build/css/',
		    ext: '.css'
		}]
	    }
	},
	watch: {
	    sass: {
		files: ['**/*.scss'],
		tasks: ['sass:dev']
	    }
	}
    });

    // Load uglify
    grunt.loadNpmTasks('grunt-contrib-uglify');

    // Load sass
    grunt.loadNpmTasks('grunt-contrib-sass');

    // Load watch
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default tasks
    grunt.registerTask('default', ['uglify', 'sass:dist']);

};
