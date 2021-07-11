# url-shortener

New project name url-shortener
~~~
oc new-project url-shortener
~~~

Deploy url-shortener
~~~
oc new-app python~https://github.com/cheevatee/url-shortener -e APP_FILE=url-shortener.py
oc expose svc url-shortener
oc get route
~~~

Create script for re-deploy url-shortener
~~~
cat <<EOF >> deploy-url-shortener.sh
oc project url-shortener
oc delete all --all -n url-shortener
oc new-app python~https://github.com/cheevatee/url-shortener -e APP_FILE=url-shortener.py -n url-shortener
sleep 10
oc logs -f url-shortener-1-build -n url-shortener
oc expose svc url-shortener -n url-shortener
sleep 5
oc get po -o wide -n url-shortener
oc get route -n url-shortener
EOF
chmod 755 deploy-url-shortener.sh
~~~

Re-deploy url-shortener

~~~
./deploy-url-shortener.sh
~~~
