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

secretArn=`aws secretsmanager list-secrets --filters Key=name,Values=MQBrokerUserPasswordSecret | jq '.SecretList[] | {ARN}' | grep 'ARN' | cut -d '"' -f4`
brokerUser=`aws secretsmanager get-secret-value --secret-id $secretArn | jq -r '.SecretString' | tr -d '{}' | sed 's/"//g' | cut -d',' -f1 | cut -d':' -f2`
brokerPassword=`aws secretsmanager get-secret-value --secret-id $secretArn | jq -r '.SecretString' | tr -d '{}' | sed 's/"//g' | cut -d',' -f2 | cut -d':' -f2`

echo export BROKER_ENDPOINT=$privateBrokerEndpoint >> ~/.bashrc;
echo export PUBLIC_BROKER_ENDPOINT=$publicBrokerEndpoint >> ~/.bashrc; 

echo export BROKER_USER=$brokerUser >> ~/.bashrc; 
echo export BROKER_PASSWORD=$brokerPassword >> ~/.bashrc;  

source ~/.bashrc
