# include pathは適当に設定しています。調整して実行してください。
LOG4G_PATH=${HOME}/.m2/repository/org/apache/logging/log4j/log4j-core/2.14.1/log4j-core-2.14.1.jar:${HOME}/.m2/repository/org/apache/logging/log4j/log4j-api/2.14.1/log4j-api-2.14.1.jar
SENTRY_PATH=${HOME}/.m2/repository/io/sentry/sentry/6.23.0/sentry-6.23.0.jar:${HOME}/.m2/repository/com/google/code/gson/gson/2.8.6/gson-2.8.6.jar:${HOME}/.m2/repository/io/sentry/sentry-log4j2/6.23.0/sentry-log4j2-6.23.0.jar


CLASSPATH=target/solver-1.0.jar:${LOG4G_PATH}:${SENTRY_PATH}

build:
	# mvn clean install
	mvn clean package

run: build
	java -classpath ${CLASSPATH} solver.Solver
