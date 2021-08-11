echo "Installing rabbitmq cli..."
wget https://raw.githubusercontent.com/rabbitmq/rabbitmq-management/v3.8.9/bin/rabbitmqadmin
chmod u+x rabbitmqadmin 


cd ~/environment
echo "Installing jq..."
sudo yum install -y jq > /dev/null 2>&1
echo "Installing pika..."
sudo pip install pika

privateBrokerId=`aws mq list-brokers | jq '.BrokerSummaries[] | select(.BrokerName=="RabbitWorkshopBrokerPrivate") | {id:.BrokerId}' | grep "id" | cut -d '"' -f4`
privateBrokerEndpoint=`aws mq describe-broker --broker-id $privateBrokerId | jq -r '.BrokerInstances[] | .ConsoleURL | split("//")[1]'`

publicBrokerId=`aws mq list-brokers | jq '.BrokerSummaries[] | select(.BrokerName=="RabbitWorkshopBrokerPublic") | {id:.BrokerId}' | grep "id" | cut -d '"' -f4`
publicBrokerEndpoint=`aws mq describe-broker --broker-id $publicBrokerId | jq -r '.BrokerInstances[] | .ConsoleURL | split("//")[1]'`


echo BROKER_ENDPOINT=$privateBrokerEndpoint >> ~/.bashrc;
echo PUBLIC_BROKER_ENDPOINT=$publicBrokerEndpoint >> ~/.bashrc; 


echo BROKER_USER='workshopuser' >> ~/.bashrc; 
echo BROKER_PASSWORD='workshopPassw0rd' >> ~/.bashrc;  


source ~/.bashrc