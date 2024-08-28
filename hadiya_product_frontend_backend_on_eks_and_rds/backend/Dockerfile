FROM node:16

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install Node.js dependencies
RUN npm install

# Copy the application files to the working directory
COPY . .

# Expose the port your app will run on
EXPOSE 3000

# Command to run your application
#CMD ["npm", "run","pm2start"]

# Command to running your apps using 
# CMD ["npm", "run","pm2logs"]

CMD ["bash", "-c", "npm run pm2logs & npm run start"]
